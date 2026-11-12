from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.dataset import Dataset
from app.schemas.dataset import DatasetCreate, DatasetRead


router = APIRouter(
    prefix="/datasets",
    tags=["Datasets"],
)


@router.post("/", response_model=DatasetRead, status_code=201)
def create_dataset(
    data: DatasetCreate,
    db: Session = Depends(get_db),
):
    dataset = Dataset(
        name=data.name,
        description=data.description,
    )

    db.add(dataset)
    db.commit()
    db.refresh(dataset)

    return dataset


@router.get("/", response_model=list[DatasetRead])
def list_datasets(
    db: Session = Depends(get_db),
):
    statement = select(Dataset).order_by(Dataset.created_at.desc())
    datasets = db.scalars(statement).all()

    return datasets