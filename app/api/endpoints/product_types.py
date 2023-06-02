from typing import Any, List, Annotated, Union
from fastapi import APIRouter, Depends, Body, Query, HTTPException
from sqlalchemy.orm import Session

from app.api import deps
from app import schemas, models, crud

router = APIRouter()


@router.post('/me', response_model=schemas.ProductType)
def create_product_type_me(
    *,
    db: Session = Depends(deps.get_db),
    obj_in: schemas.ProductTypeCreate,
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """
    Create product-type for current user
    """
    category = crud.category.get(db, id=obj_in.category_id)
    if not category or category.owner_id != current_user.id:
        raise HTTPException(
            status_code=404,
            detail="The category with this id does not exist in the system"
        )
    
    return crud.product_type.create(db, obj_in=obj_in)


@router.get('/me', response_model=List[schemas.ProductType])
def read_product_types_me(
    *,
    db: Session = Depends(deps.get_db),
    limit: int = 100,
    skip: int = 0,
    category_id: Annotated[Union[int, None], Query(description='filtering by category')] = None,
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """
    List current user's product-types
    """
    if not category_id:
        return crud.product_type.get_multi_by_owner(db, owner_id=current_user.id)

    category = crud.category.get(db, category_id)
    if not category or category.owner_id != current_user.id:
        raise HTTPException(
            status_code=404,
            detail="The category with this id does not exist in the system"
        )
    
    return crud.product_type.get_multi_by_category(db=db, category_id=category_id, limit=limit, skip=skip)


# Admin endpoints

@router.get('', response_model=List[schemas.ProductType])
def read_product_types(
    *,
    db: Session = Depends(deps.get_db),
    limit: int = 100,
    skip: int = 0,
    current_user: models.User = Depends(deps.get_current_active_superuser)
) -> Any:
    """
    List all product-types
    """
    return crud.product_type.get_multi(db, skip=skip, limit=limit)


@router.post('', response_model=schemas.ProductType)
def create_product_type_me(
    *,
    db: Session = Depends(deps.get_db),
    obj_in: schemas.ProductTypeCreate,
    current_user: models.User = Depends(deps.get_current_active_superuser)
) -> Any:
    """
    Create product-type
    """
    category = crud.category.get(db, id=obj_in.category_id)
    if not category:
        raise HTTPException(
            status_code=404,
            detail="The category with this id does not exist in the system"
        )

    return crud.product_type.create(db, obj_in=obj_in)