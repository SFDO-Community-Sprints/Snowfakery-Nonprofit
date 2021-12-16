"""Provider for Faker which adds fake nonprofit names, and program names."""

import faker.providers

PREFIXES = [
    '',
    '1st',
    '2nd',
    'Best',
    'Eastern',
    'Friends of the',
    'Last',
    'Legal',
    'Lower',
    'Northern',
    'Southern',
    'Upper',
    'Western',
]

TOPICS = [
    'Aid',
    'Animal',
    'Doctors',
    'Dog',
    'Education',
    'Friends',
    'History',
    'Housing',
    'Justice',
    'Medical',
    'Otters',
    'Peace',
    'Pets',
    'Relief',
    'Scholarship',
    'Scouts',
    'Unity',
    'Water',
    'Whales',
]

SUFFIXES = [
    'Aid Society',
    'Agency',
    'Alliance',
    'Association',
    'Charities',
    'Center',
    'Coalition',
    'Committee',
    'Community',
    'Council',
    'Defense Fund',
    'Foundation',
    'Fund',
    'Gathering',
    'Home',
    'Hospital',
    'House',
    'Institute',
    'International',
    'Mission',
    'Network',
    'People',
    'Rights Watch',
    'Service',
    'Society',
    'Trust',
    'United',
]


class Provider(faker.providers.BaseProvider):
    """Provider for Faker which adds fake nonprofit information."""

    def nonprofit_name(self):
        """Fake nonprofit names."""
        prefix = self.random_element(PREFIXES)
        suffix = self.random_element(SUFFIXES)
        topic = self.random_element(TOPICS)

        return " ".join([prefix, topic, suffix]).strip()
