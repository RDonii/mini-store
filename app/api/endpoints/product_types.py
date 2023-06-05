from typing import Any, List, Annotated, Union
from fastapi import APIRouter, Depends, Query, HTTPException
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

@router.get('/{product_type_id}', response_model=schemas.ProductType)
def read_product_type(
    *,
    db: Session = Depends(deps.get_db),
    product_type_id: int,
    current_user: models.User = Depends(deps.get_current_active_user)
):
    """
    Get a specific product-type
    """
    pt = crud.product_type.get(db, id=product_type_id)
    if not pt or (not crud.user.is_superuser(current_user) and pt.category.owner_id != current_user.id):
        raise HTTPException(
            status_code=404,
            detail="The product-type with this id does not exist in the system"
        )

    return pt


@router.put('/{product_type_id}', response_model=schemas.ProductType)
def update_product_type(
    *,
    db: Session = Depends(deps.get_db),
    product_type_id: int,
    obj_in: schemas.product_type.ProductTypeUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
):
    """
    Update a specific product-type
    """
    pt = crud.product_type.get(db, id=product_type_id)
    if not pt or (crud.user.is_superuser(current_user) and pt.category.owener_id != current_user.id):
        raise HTTPException(
            status_code=404,
            detail="The product-type with this id does not exist in the system"
        )

    return crud.product_type.update(db, db_obj=pt, obj_in=obj_in)


@router.delete('/{product_type_id}', response_model=schemas.ProductType)
def delete_product_type(
    *,
    db: Session = Depends(deps.get_db),
    product_type_id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
):
    """
    Delete a specific product-type
    """
    pt = crud.product_type.get(db, id=product_type_id)
    if not pt or (not crud.user.is_superuser(current_user) and pt.category.owner_id != current_user.id):
        raise HTTPException(
            status_code=404,
            detail="The product-type with this id does not exist in the system"
        )

    return crud.product_type.remove(db, id=product_type_id)


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
def create_product_type(
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