from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError

modifiers = ['-', 'm', 'b', 'd']
bases = ['A', 'G', 'C', 'T', 'U', 'R', 'Y', 'S', 'W', 'K', 'M', 'B', 'D', 'H', 'V', 'N']
sugars = ['d', 'r', 'e', 'm', 'y', 'l', 'k', 'o']
linkers = ['o', 's']

def make_error_message(i, char, condition):
	return 'Failure at bp {}, {} is not a valid {}'.format(i, char, condition)

def validate_sequence_design(seq_design):
	i = 0
	while i < len(seq_design):
		modifier = seq_design[i]
		base = seq_design[i+1]
		sugar = seq_design[i+2]
		if modifier not in modifiers:
			message =  make_error_message(i + 1, modifier, 'modifier')
			raise ValidationError(message, params={'design': seq_design})
		elif base not in bases:
			message = make_error_message(i + 2, base, 'base')
			raise ValidationError(message, params={'design': seq_design})
		elif sugar not in sugars:
			message =  make_error_message(i + 3, sugar, 'sugar')
			raise ValidationError(message, params={'design': seq_design})

		if i + 3 < len(seq_design):
			linker = seq_design[i+3]
			if linker not in linkers:
				message = make_error_message(i + 4, linker, 'linker')
				raise ValidationError(message, params={'design': seq_design})
		i += 4

class Sequence(models.Model):
	design = models.TextField(validators=[validate_sequence_design])
	name = models.CharField(max_length=50)
	owner = models.CharField(max_length=25)
	description = models.CharField(max_length=1000, blank=True)

	@property
	def formatted(self):
		i = 0
		formatted_seq = ''
		state = 'r' # start out in RNA state so opening bracket is added if needed
		while i < len(self.design):
			letter = self.design[i + 1]
			backbone = self.design[i + 2]
			if backbone == state:
				formatted_seq += letter
			elif backbone == 'd' and state == 'r':
				formatted_seq += '[' + letter
				state = 'd'
			elif backbone == 'r' and state == 'd':
				formatted_seq += ']' + letter
				state = 'r'
			i += 4

		# checks to see if final closing bracket is needed
		if state == 'd':
			formatted_seq += ']'

		return formatted_seq

class Chain(models.Model):
    """ High-level retail chain model"""
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    slogan = models.CharField(max_length=500)
    founded_date = models.CharField(max_length=500)
    website = models.URLField(max_length=500)


class Store(models.Model):
    """ Store location model.  Foreign key to Chain."""
    chain = models.ForeignKey(Chain)
    number = models.CharField(max_length=20)
    address = models.CharField(max_length=1000)
    opening_date = models.DateTimeField(default=timezone.now)

    # Business hours in a 24 hour clock.  Default 8am-5pm.
    business_hours_start = models.IntegerField(
        default=8,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(23)
        ]
    )
    business_hours_end = models.IntegerField(
        default=17,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(23)
        ]
    )


class Employee(models.Model):
    """ Location employee model.  Foreign key to Store."""
    store = models.ForeignKey(Store)
    number = models.CharField(max_length=20)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    hired_date = models.DateTimeField(default=timezone.now)
