from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api import deps
from app import models, schemas, crud


router = APIRouter()


@router.post('/me', response_model=schemas.Product)
def create_product_me(
    *,
    db: Session = Depends(deps.get_db),
    obj_in: schemas.ProductCreate,
    current_user: models.User = Depends(deps.get_current_active_user)
):
    """
    Create product for current user
    """
    product_type = crud.product_type.get_multi_by_owner(db, id=obj_in.type_id, owner_id=current_user.id)
    if len(product_type) == 0:
        raise HTTPException(
            status_code=404,
            detail="The product-type with this id does not exist in the system"
        )
    
    return crud.product.create(db, obj_in=obj_in)


@router.get('/me', response_model=List[schemas.Product])
def read_products_me(
    *,
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user)
):
    """
    List current user's products
    """
    return crud.product.get_multi_by_owner(db, skip=skip, limit=limit, owner_id=current_user.id)


# Admin endpoints

@router.get('', response_model=List[schemas.Product])
def read_products(
    *,
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_superuser)
):
    """
    List products
    """
    return crud.product.get_multi(db, skip=skip, limit=limit)


@router.post('', response_model=schemas.Product)
def create_product(
    *,
    db: Session = Depends(deps.get_db),
    obj_in: schemas.ProductCreate,
):
    """
    Create product
    """
    product_type = crud.product_type.get(db, id=obj_in.type_id)
    if not product_type:
        raise HTTPException(
            status_code=404,
            detail="The product-type with this id does not exist in the system"
        )

    return crud.product.create(db, obj_in=obj_in)
