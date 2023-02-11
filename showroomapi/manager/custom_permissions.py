"""Module for Making custom Permissions"""
from rest_framework.permissions import BasePermission


class IsManager(BasePermission):
    """ For Manager returns True """
    def has_permission(self, request, view):
        # checking for anonymous users
        try:
            # returns true or false
            user = request.user.is_manager
        except AttributeError:
            return False

        return user


class IsAdvisor(BasePermission):
    """ For Advisor returns True """
    def has_permission(self, request, view):
        try:
            user = request.user.is_advisor
        except AttributeError:
            return False

        return user


class IsMechanic(BasePermission):
    """ For Mechanic returns True """
    def has_permission(self, request, view):
        # checking for anonymous users
        try:
            # returns true or false
            user = request.user.is_mechanic
        except AttributeError:
            return False

        return user


class IsFrontDesk(BasePermission):
    """ For Front desk employee returns True """
    def has_permission(self, request, view):
        # checking for anonymous users
        try:
            # returns true or false
            user = request.user.is_manager
        except AttributeError:
            return False

        return user
