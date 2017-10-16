from django import forms
from django import template

register = template.Library()


@register.filter(name='date_sort')
def date_sort(instance):
    return instance.order_by("-id")


@register.inclusion_tag('widgets/breadcrumb.html')
def breadcrumb(steps):
    return dict(steps=steps)


@register.inclusion_tag('widgets/menubar.html', takes_context=True)
def menubar(context, project=None, edit_project=False, create_project=False,
            data=None, edit_data=False, upload_data=False,
            analysis=None, edit_analysis=False
            ):

    user = context.request.user

    return dict(
        user=user,
        project=project, edit_project=edit_project, create_project=create_project,
        data=data, edit_data=edit_data, upload_data=upload_data,
        analysis=analysis, edit_analysis=edit_analysis,
    )


@register.filter(name='is_checkbox')
def is_checkbox(value):
    return isinstance(value, forms.BooleanField)
