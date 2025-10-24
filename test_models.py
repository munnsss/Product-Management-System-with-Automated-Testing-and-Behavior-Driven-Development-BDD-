# tests/test_models.py
import pytest
from service.models import Product
from tests.factories import ProductFactory

@pytest.fixture
def sample_product():
    # Create a fake product
    product = ProductFactory()
    product.save()  # Assuming your Product model has a save() method
    return product

def test_read_product(sample_product):
    # Attempt to read the product by ID
    retrieved_product = Product.get_by_id(sample_product.id)
    
    # Assertions to verify it was read correctly
    assert retrieved_product is not None
    assert retrieved_product.id == sample_product.id
    assert retrieved_product.name == sample_product.name
    assert retrieved_product.category == sample_product.category
    assert retrieved_product.price == sample_product.price
    assert retrieved_product.availability == sample_product.availability
