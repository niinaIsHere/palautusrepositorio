class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True


class Or:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if matcher.test(player):
                return True

        return False


class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team


class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value


class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value < self._value


class Not:
    def __init__(self, operation):
        self.operation = operation

    def test(self, player):
        if self.operation.test(player):
            return False
        else:
            return True


class All:
    def __init__(self):
        pass

    def test(self, player):
        if player:
            return True


class QueryBuilder:
    def __init__(self):
        self.query = []
        self.state = 'AND'

    def build(self):
        if len(self.query) == 0:
            self.all()
        if self.state == 'AND':
            return And(*self.query)
        return Or(*self.query)
    
    def plays_in(self, team):
        self.query.append(PlaysIn(team))
        return self

    def has_at_least(self, value, attribute):
        self.query.append(HasAtLeast(value, attribute))
        return self

    def has_fewer_than(self, value, attribute):
        self.query.append(HasFewerThan(value, attribute))
        return self
    
    def has_not(self, operation):
        self.query.append(Not(operation))
        return self
    
    def all(self):
        self.query.append(All())
        return self
