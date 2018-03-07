import models
import store

member1 = models.Member("Ali Najjar", 26)
member2 = models.Member("Muhammad Najjar", 29)

post1 = models.Post("first post", "Hello, I am Ali")
post2 = models.Post("second post", "How are you")
post3 = models.Post("third post", "What do you do")

print member1
print post1

member_store = store.MemberStore()
member_store.add(member1)
a = member_store.get_all()
print a

post_store = store.PostStore()
post_store.add(post1)
b = post_store.get_all()
print b
