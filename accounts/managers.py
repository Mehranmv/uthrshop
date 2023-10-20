from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email,phone_number, full_name, password):
        if not phone_number:
            raise ValueError('user most have phone number')
        if not email:
            raise ValueError('user most have email')
        if not full_name:
            raise ValueError('user most have full name')

        user = self.model(
            email=self.normalize_email(email),
            phone_number=phone_number,
            full_name=full_name
        )
        user.set_password(
            password
        )
        user.save(
            using=self._db
        )
        return user

    def create_superuser(self, email,phone_number, full_name, password):
        user = self.create_user(
            email=email,
            phone_number=phone_number,
            full_name=full_name,
            password=password
        )
        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)
        return user
