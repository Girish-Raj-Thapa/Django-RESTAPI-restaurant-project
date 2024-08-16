from rest_framework import serializers

from .models import Category, MenuItem, Cart, Order, OrderItem
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


# Serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'slug', 'title']


class MenuItemSerializer(serializers.ModelSerializer):
    # Relationship between CategorySerializer and MenuItemSerializer
    category = CategorySerializer(read_only=True)

    # category_id --> to specify category for each item
    category_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'feature', 'category', 'category_id']


class CartHelpSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price']


class CartSerializer(serializers.ModelSerializer):
    menuitem = CartHelpSerializer()

    class Meta:
        model = Cart 
        fields = ['menuitem', 'quantity', 'price']


class CartAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart 
        fields = ['menuitem', 'quantity']
        extra_kwargs = {
            'quantity':{'min_value':1},
        }


class CartRemoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['menuitem']
    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        field = ['username']


class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Order 
        field = ['id', 'user', 'delivery_crew', 'status', 'total', 'date']


class SingleHelperSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem 
        fields = ['title', 'price']


class SingleOrderSerializer(serializers.ModelSerializer):
    menuitem = SingleHelperSerializer()
    class Meta:
        model = OrderItem 
        fields = ['menuitem', 'quantity']


class OrderInsertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order 
        fields = ['delivery_crew']


class ManagerListSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(read_only=True)  # Make email field read-only
    class Meta:
        model = User 
        fields = ['id', 'username', 'email']