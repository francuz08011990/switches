from django.db import models


class SwitchVendor(models.Model):
    title = models.CharField('Vendor', max_length=70)

    class Meta:
        verbose_name = 'Vendor'
        verbose_name_plural = 'Vendors'

    def __str__(self):
        return self.title


class UserPlace(models.Model):
    id = models.AutoField(primary_key=True)
    street = models.CharField('Street', max_length=100)
    ip = models.GenericIPAddressField('IP')
    mac = models.CharField('MAC', max_length=100)
    active = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'User place'
        verbose_name_plural = 'User places'

    def __str__(self):
        return '{0}; - IP:{1}, MAC:{2}'.format(self.street, self.ip, self.mac)


class SwitchModel(models.Model):
    title = models.CharField('Model', max_length=100)
    switch_vendor = models.ForeignKey(SwitchVendor, on_delete=models.CASCADE, verbose_name='Vendor of switch',
                                      related_name='models')
    user_place = models.ForeignKey(UserPlace, on_delete=models.CASCADE, verbose_name='User Place',
                                   related_name='models')
    ports = models.PositiveSmallIntegerField('Number of ports')

    class Meta:
        verbose_name = 'Model'
        verbose_name_plural = 'Models'

    def __str__(self):
        return '%s - vendor is: %s' % (self.title, self.switch_vendor)


class User(models.Model):
    first_name = models.CharField('First name', max_length=50)
    last_name = models.CharField('Last name', max_length=150)
    flat = models.IntegerField('Apartment number')
    installation_place = models.ForeignKey(UserPlace, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Installation place',
                                           related_name='users')

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    @property
    def full_name(self):
        return '{} {}'.format(self.last_name, self.first_name)

    def __str__(self):
        return '%s, number of apartment: %d' % (self.full_name, self.flat)
