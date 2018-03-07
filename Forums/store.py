class MemberStore:

    members = []
    last_id = 1

    def get_all(self):
        return MemberStore.members

    def add(self, member):
        MemberStore.members.append(member)
        member.id = MemberStore.last_id
        MemberStore.last_id += 1

    def get_by_id(self, id):
        all_members = self.get_all()
        for member in all_members:
            if member.id == id:
                return member
            else:
                return None

    def entity_exists(self, member):
        result = True
        member = self.get_by_id(member.id)
        if member is None:
            result = False
        return result

    def delete(self, id):
        member = self.get_by_id(id)
        if member.id == id:
            MemberStore.members.remove(member)
            return "the member is deleted"


class PostStore:

    posts = []

    def get_all(self):
        return PostStore.posts

    def add(self, post):
        PostStore.posts.append(post)
