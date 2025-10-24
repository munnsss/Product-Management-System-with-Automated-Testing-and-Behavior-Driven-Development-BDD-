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



updated file

# tests/test_models.py
import pytest
from service.models import Product
from tests.factories import ProductFactory

@pytest.fixture
def sample_product():
    # Create a fake product
    product = ProductFactory()
    product.save()  # Ensure the product is saved
    return product

def test_update_product(sample_product):
    # Update product details
    updated_name = "UpdatedName"
    updated_price = 999
    sample_product.name = updated_name
    sample_product.price = updated_price
    sample_product.save()  # Save changes to the database

    # Retrieve the product again to verify updates
    retrieved_product = Product.get_by_id(sample_product.id)

    # Assertions to check if update was successful
    assert retrieved_product.name == updated_name
    assert retrieved_product.price == updated_price
    assert retrieved_product.category == sample_product.category  # unchanged
    assert retrieved_product.availability == sample_product.availability  # unchanged


