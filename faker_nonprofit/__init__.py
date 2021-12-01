"""Provider for Faker which adds fake nonprofit names, and program names."""

import faker.providers

PREFIXES = [
    '',
    '1st',
    'Eastern',
    'Friends of the',
    'Lower',
    'Northern',
    'Southern',
    'Upper',
    'Western'
]

TOPICS = [
    'Animal',
    'Friends',
    'History',
    'Peace',
    'Pets',
    'Unity'
]

SUFFIXES = [
    'Alliance',
    'Asscociation',
    'Center',
    'Committee',
    'Community',
    'Foundation',
    'Gathering',
    'Home',
    'Institute',
]


class Provider(faker.providers.BaseProvider):
    """Provider for Faker which adds fake nonprofit information."""

    def nonprofit_name(self):
        """Fake nonprofit names."""
        prefix = self.random_element(PREFIXES)
        suffix = self.random_element(SUFFIXES)
        topic = self.random_element(TOPICS)

        return " ".join([prefix, topic, suffix]).strip()
