from allauth.account.adapter import DefaultAccountAdapter


class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=False):
        user = super().save_user(request, user, form, commit)
        data = form.cleaned_data
        user.age = data.get('age')
        user.place = data.get('place')
        user.contact = data.get('contact')

        user.save()
        return user
