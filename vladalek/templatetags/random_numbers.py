import random
from django import template

register = template.Library()

@register.simple_tag
def random_image(images):
	return random.choice(images)