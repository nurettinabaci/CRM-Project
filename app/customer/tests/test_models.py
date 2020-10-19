from django.test import TestCase
from django.contrib.auth import get_user_model

from ..models import Customer
from model_bakery import baker

import datetime


class ModelTest(TestCase):

    def test_create_user_with_email_successfull(self):
        '''Test creating a new user with an email successful'''
        username = 'testname'
        email = 'test@nurettinapp.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            username=username,
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_user_email_normalized(self):
        '''Test the email for a new user is normalized'''
        email = 'test@NURETTINAPP.com'
        user = get_user_model().objects.create_user(username='testname',
                                                    email=email,
                                                    password='Testpass1234')

        self.assertEqual(user.email, email.lower())

    def test_create_new_superuser(self):
        '''Test creating new superuser'''
        user = get_user_model().objects. \
            create_superuser(username='s_user',
                             email='test@nurettinapp.com',
                             password='Testpass1234')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_customer(self):
        '''Test creating new customer'''
        customer = Customer.objects.create(
            first_name='customer first name',
            last_name='customer last name',
            tc='1515555555',
            phone='01515555555',
        )
        customer_res = Customer.objects.last()

        self.assertEqual(customer.id, customer_res.id)

    def test_update_customer(self):
        '''Test update a customer'''
        customer = Customer.objects.create(
            first_name='customer first name',
            last_name='customer last name',
            tc='1515555555',
            phone='01515555555',
        )
        customer_res = Customer.objects.last()
        customer_res.last_name = 'new last name'
        customer_res.save()
        customer_res2 = Customer.objects.last()

        self.assertNotEqual(customer.last_name, customer_res.last_name)
        self.assertEqual(customer_res.last_name, customer_res2.last_name)

    def test_delete_customer(self):
        '''Test delete a customer'''
        Customer.objects.create(
            first_name='customer first name',
            last_name='customer last name',
            tc='1515555555',
            phone='01515555555',
        )
        Customer.objects.all().delete()
        customers = Customer.objects.all()

        self.assertEqual(len(customers), 0)

    def test_customer_str(self):
        '''Test the customer string representation'''
        customer = Customer.objects.create(
            first_name='customer first name',
            last_name='customer last name',
            tc='1515555555',
            phone='01515555555',
        )
        self.assertEqual(str(customer), customer.tc)

    def test_customer_speedtest(self):
        '''Speed test with 1000 create customer instance'''
        NUM_CUSTOMER = 1000
        start_time = datetime.datetime.now()
        customers = baker.make('customer.Customer', _quantity=NUM_CUSTOMER)
        end_time = datetime.datetime.now()
        with open('customer_create_speedtest.txt', mode='a',
                  encoding='utf-8', newline='\n') as f:
            f.write(''.join([
                f'Create {NUM_CUSTOMER} customer instances: ',
                str(end_time - start_time),
                '\n'
            ]))
            self.assertEqual(len(customers), NUM_CUSTOMER)
