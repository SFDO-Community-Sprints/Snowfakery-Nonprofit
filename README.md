# Snowfakery-Nonprofit

Faker provider for generating data specific to non-profit use-cases.

Supported by the Salesforce Open Source Commons community to work with Snowfakery.


## Installation

Install with pip

`pip install faker-nonprofit`

## Faker Use

Once Faker and this provider are installed, you should be able to run the following script from any place on your system.

```python
from faker import Faker
import faker_nonprofit

fake = Faker()
fake.add_provider(faker_nonprofit.Provider)

for _ in range(10):
  print(fake.nonprofit_name())
```

## Snowfakery Use

For now you will need to clone the repository and then follow the example in the [sample recipe](snowfakery_nonprofit_example.recipe.yml).
