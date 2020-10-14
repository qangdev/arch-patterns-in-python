import repository_pattern.model as model
import repository_pattern.repository as repository


def test_repository_can_save_a_batch(session):
    batch = model.Batch("batch_1", "RUSTY-SOAPDISH", 100, eta=None)

    repo = repository.SqlAlchemyRepository(session)
    repo.add(batch)
    session.commit()

    rows = list(session.execute("SELECT reference, sku, _purchased_quantity, eta FROM batches"))
    assert rows == [("batch_1", "RUSTY-SOAPDISH", 100, None)]