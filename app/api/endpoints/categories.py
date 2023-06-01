from typing import List, Any
from fastapi import APIRouter, Depends, Body, HTTPException
from sqlalchemy.orm import Session

from app.api import deps
from app import models, schemas, crud


router = APIRouter()


@router.post('/me', response_model=schemas.Category)
def create_category_me(
    *,
    db: Session = Depends(deps.get_db),
    title: str = Body(),
    description: str = Body(None),
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """
    Create category for current user
    """
    category = crud.category.get_by_title_owner(db, owner_id=current_user.id, title=title)
    if category:
        raise HTTPException(
            status_code=400,
            detail="The category with this title already exists in the system.",
        )
    obj_in = schemas.CategoryCreate(title=title, description=description, owner_id=current_user.id)
    return crud.category.create(db, obj_in=obj_in)


@router.get('/me', response_model=List[schemas.Category])
def read_categories_me(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """
    List categories of current user
    """
    return crud.category.get_multi_by_owner(db, owner_id=current_user.id, skip=skip, limit=limit)


@router.get('/{category_id}', response_model=schemas.Category)
def read_category(
    *,
    db: Session = Depends(deps.get_db),
    category_id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get a specific category
    """
    category = crud.category.get(db, id=category_id)
    if not category or not crud.user.is_superuser(current_user) and category.owner_id != current_user.id:
        raise HTTPException(
            status_code=404,
            detail="The category with this id does not exist in the system"
        )
    return category


@router.put('/{category_id}', response_model=schemas.Category)
def update_category(
    *,
    db: Session = Depends(deps.get_db),
    category_id: int,
    category_in: schemas.CategoryUpdate,
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """
    Update a specific category
    """
    category = crud.category.get(db, category_id)
    if not category or not crud.user.is_superuser(current_user) and category.id == current_user.id:
        raise HTTPException(
            status_code=404,
            detail="The category with this title already exists in the system.",
        )
    return crud.category.update(db, db_obj=category, obj_in=category_in)


# Admin endpoints

@router.post('', response_model=schemas.Category)
def create_category(
    *,
    db: Session = Depends(deps.get_db),
    obj_in: schemas.CategoryCreate,
    current_user: models.User = Depends(deps.get_current_active_superuser)
):
    """
    Create category
    """
    category = crud.category.get_by_title_owner(db, owner_id=obj_in.owner_id, title=obj_in.title)
    if category:
        raise HTTPException(
            status_code=400,
            detail="The category with this title already exists in the system.",
        )
    return crud.category.create(db, obj_in=obj_in)


@router.get('', response_model=List[schemas.Category])
def list_categories(
    *,
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_superuser)
):
    return crud.category.get_multi(db, skip=skip, limit=limit)
