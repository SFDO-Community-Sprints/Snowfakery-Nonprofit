"""Provider for Faker which adds fake nonprofit names, and program names."""

import faker.providers
from faker.generator import Generator
import faker.providers.address.en_US
# @todo when our more diverse provider is ready this should be replaced by that.
import faker.providers.person.en_US

PREFIXES = [
    '',
    '1st',
    '2nd',
    'Best',
    'Eastern',
    'Friends of the',
    'Legal',
    'Lower',
    'Northern',
    'Southern',
    'Upper',
    'Western',
]

TOPICS = [
    'Advocates',
    'Aid',
    'Animal',
    'Baptist',
    'Catholic',
    'Cats',
    'Doctors',
    'Dogs',
    'Education',
    'Episcopal',
    'Friends',
    'Guinea Pigs',
    'Hindu',
    'History',
    'Horse',
    'Housing',
    'Humane',
    'Islamic',
    'Jewish',
    'Justice',
    'Medical',
    'Methodist',
    'Mormon',
    'Otters',
    'Peace',
    'Pets',
    'Pika',
    'Presbyterian',
    'Rabbits',
    'Relief',
    'Scholarship',
    'Scouts',
    'Survivors',
    'Unitarian',
    'Unity',
    'Water',
    'Whales',
]

SUFFIXES = [
    'Agency',
    'Aid Society',
    'Alliance',
    'Association',
    'Center',
    'Charities',
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

JOB_TITLES = [
    'Accountant',
    'Administrative Assistant',
    'Advocacy Director',
    'Associate Director',
    'Board Member',
    'Business Office Supervisor',
    'Case Manager',
    'Chemical Dependency Director',
    'Chief Association Executive',
    'Chief Operating Officer',
    'Communications Director',
    'Community Health Director',
    'Community Relations Director',
    'Community Service Program Coordinator',
    'Community Service Project Coordinator',
    'Compliance Coordinator',
    'Compliance Director',
    'Coordinator Of Planned Giving',
    'Corporate Giving Director',
    'Corporate Giving Manager',
    'Critical Care Director',
    'Development Assistant',
    'Development Associate',
    'Development Coordinator',
    'Development Director',
    'Development Manager',
    'Development Officer',
    'Director',
    'Director Of Community Relations',
    'Director Of Family Shelter',
    'Director Of Major Gifts',
    'Director Of Philanthropy',
    'Director Of Special Initiatives',
    'Donor Relations Manager',
    'Event Team Recruiter',
    'Executive Director',
    'Financial Aid Director',
    'Financial Aid Representative',
    'Foundation Director',
    'Foundation Program Officer',
    'Fundraising Coordinator',
    'Fundraising Manager',
    'Grant Administrator',
    'Grant And Contracts Specialist',
    'Grant Coordinator',
    'Grant Proposal Manager',
    'Housing Program Manager',
    'Human Resources Representative',
    'IT Manager',
    'IT Specialist',
    'Information Technology Manager',
    'Job Developer',
    'Major Gift Director',
    'Medical Social Worker',
    'Member Certification Manager',
    'Member Records Administrator',
    'Member Services Director',
    'Member Services Representative',
    'Membership Assistant',
    'Nonprofit Fundraiser',
    'Office Manager',
    'Planned Giving Director',
    'Planning Manager',
    'Policy Analyst',
    'Program Assistant',
    'Program Associate',
    'Program Center Director',
    'Program Coordinator',
    'Program Director',
    'Program Manager',
    'Program Officer For Foundation',
    'Project Manager',
    'Public Relations Manager',
    'Recruiter',
    'Shelter Director',
    'Social Services Director',
    'Social Work Manager',
    'Special Events Director',
    'Support Services Director',
    'Team Leader',
    'Volunteer Coordinator',
    'Volunteer Director',
    'Volunteer Manager',
    'Volunteer Services Director',
    'Web Director',
]


class Provider(faker.providers.BaseProvider):
    """Provider for Faker which adds fake nonprofit information."""

    def nonprofit_name(self):
        """Fake nonprofit names."""
        prefix = self.random_element(PREFIXES)
        suffix = self.random_element(SUFFIXES)
        topic = self.random_element(TOPICS)

        name = " ".join([prefix, topic, suffix]).strip()
        if suffix == "Foundation" or suffix == "Fund":
            name = self.foundation_name()

        return name

    def nonprofit_title(self):
        """Fake nonprofit job titles."""
        return self.random_element(JOB_TITLES)

    def foundation_name(self):
        """Fake foundation names."""
        nameType = self.random_element(['City', 'Other', 'Person', 'State'])
        prefix = ""
        if (nameType == 'City'):
            prefix = self.generator.city()
        elif (nameType == 'Person'):
            if self.random_element(['Full', 'Family']) == 'Full':
                prefix = self.generator.first_name() + ' ' + self.generator.last_name()
            else:
                prefix = self.generator.last_name() + ' Family'
        elif (nameType == 'State'):
            prefix = self.generator.state()
        else:
            prefix = " ".join([self.random_element(PREFIXES), self.random_element(TOPICS)]).strip()

        suffix =self.random_element(['Foundation', 'Fund'])
        name = " ".join([prefix, suffix]).strip()

        return name
