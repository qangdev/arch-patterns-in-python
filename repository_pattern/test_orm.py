from .orm import model

def test_orm_here(session):
    assert 1 + 1 == 2, "Wrong"