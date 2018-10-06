# -*- coding: utf-8 -*-
"""
DreamDict core module.
 
- Package:     dreamdict
- Version:     0.1.0
- Author:      Daniel J. Umpierrez
- Created:     06-10-2018
- Site:        https://github.com/havocesp/dreamdict
"""


class DreamDict:
    """
    Class with where keys are accessible as attributes also.
    """

    def __init__(self, **kwargs):
        """
        Class with where keys are accessible as attributes also.

        >>> data = AttrDict(strict=True, a='ABC', b=2, c=1.435)
        >>> data.a
        True
        >>> data.n = 5
        raise AttributeError()

        :param kwargs:
        :param bool strict: if True, "AttributeError" exception is raised for non existing attrs.
        """
        # self._data = dict(kwargs)
        self._strict = kwargs.pop('strict', False) or False
        self.__dict__.update(kwargs)

    def __getattr__(self, name):
        if name not in self.__dict__ and self.__dict__.get('_strict', False):
            raise AttributeError('Property "{}" not found'.format(name))
        return self.__dict__.get(name)

    def __setattr__(self, name, value):
        if not self._strict:
            self.__dict__.update({name: value})
        else:
            raise AttributeError('Property "{}" not found'.format(name))

    def __delattr__(self, name):
        if name in self.__dict__:
            del self.__dict__[name]
        elif self._strict:
            raise AttributeError('Property "{}" not found'.format(name))

    def __repr__(self):
        return '{}: {}'.format(self.__class__.__name__, self.__str__())

    def __str__(self):
        return ', '.join(['{}={}'.format(k, v) for k, v in self.__dict__.items() if k[0] != '_'])


if __name__ == '__main__':
    ad = DreamDict(strict=True, ma=1, mb='2', mc='13')
    print(ad)
    # del ad.mab
    # print(ad.mab)
    ad.mab = True
    print(ad)
