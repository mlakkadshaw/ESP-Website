" Survey models for Educational Studies Program. "

__author__    = "$LastChangedBy$"
__date__      = "$LastChangedDate$"
__rev__       = "$LastChangedRevision$"
__headurl__   = "$HeadURL$"
__license__   = "GPL v2"
__copyright__ = """
This file is part of the ESP Web Site
Copyright (c) 2007 MIT ESP

The ESP Web Site is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

Contact Us:
ESP Web Group
MIT Educational Studies Program,
84 Massachusetts Ave W20-467, Cambridge, MA 02139
Phone: 617-253-4882
Email: web@esp.mit.edu
"""

from django.contrib import admin
from esp.survey.models import Survey, SurveyResponse, QuestionType, Question, Answer

class SurveyAdmin(admin.ModelAdmin):
    pass
admin.site.register(Survey, SurveyAdmin)

class SurveyResponseAdmin(admin.ModelAdmin):
    pass
admin.site.register(SurveyResponse, SurveyResponseAdmin)
    
admin.site.register(QuestionType)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['seq', 'name', 'question_type', 'survey']
    list_display_links = ['name']
    list_filter = ['survey']
admin.site.register(Question, QuestionAdmin)

admin.site.register(Answer)
