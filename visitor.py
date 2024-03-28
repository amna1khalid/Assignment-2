#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Visitor:
    def __init__(self, name, age, email, is_student=False, is_teacher=False):
        assert isinstance(name, str) and name.strip(), "Name must be a non-empty string"
        assert isinstance(age, int) and age > 0, "Age must be a positive integer"
        assert isinstance(email, str) and '@' in email, "Invalid email address"
        
        self.name = name.strip()
        self.age = age
        self.email = email
        self.is_student = is_student
        self.is_teacher = is_teacher

class GroupVisitor(Visitor):
    def __init__(self, name, age, email, group_id):
        super().__init__(name, age, email)
        assert isinstance(group_id, str) and group_id.strip(), "Group ID must be a non-empty string"
        self.group_id = group_id.strip()

