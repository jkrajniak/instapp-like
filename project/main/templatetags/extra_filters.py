#  Copyright (C) 2017
#      Jakub Krajniak (jkrajniak at gmail.com)
#
#  This file is part of instapp.
#
#  instapp is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  instapp is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

from django import template

register = template.Library()

# Stolen from: https://benjaminbaka.wordpress.com/2016/01/23/add-class-attribute-to-django-form-fields/

@register.filter(name='addclass')
def addclass(form_field, class_attr):
    return form_field.as_widget(attrs={'class': class_attr})