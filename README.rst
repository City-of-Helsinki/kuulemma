Kuulemma
========

.. image:: https://circleci.com/gh/fastmonkeys/kuulemma.png?style=badge
    :target: https://circleci.com/gh/fastmonkeys/kuulemma

Requirements
------------

- `Python <https://www.python.org/>`_ 3.4
- `PostgreSQL <http://www.postgresql.org/>`_
- `virtualenvwrapper <http://virtualenvwrapper.readthedocs.org/>`_
- `node.js <http://nodejs.org/>`_
- `bower <http://bower.io/>`_

Development
-----------

Follow the instructions below to set up the development environment.

1. Create a new virtualenv::

    $ mkvirtualenv --python=$(which python3.4) kuulemma

2. If you are using `autoenv <https://github.com/kennethreitz/autoenv>`_, you
   can make the virtualenv activate automagically when traversing inside the
   project directory::

    $ echo -e "workon kuulemma\n" > .env

3. Install Python dependencies::

    $ pip install -r requirements-dev.txt

4. Create databases for development and testing::

    $ createdb kuulemma
    $ createdb kuulemma_test

5. Create database tables::

    $ alembic upgrade head

7. Install bower dependencies::

    $ bower install

8. Finally, start the development server::

    $ gulp

Testing
-------

- Running Python backend tests::

    $ py.test

- Running Javascript unit tests::

    $ gulp test-karma

- Running Javascript unit tests automatically when files change::

    $ gulp tdd

- Running Javascript end-to-end tests::

    $ gulp test-protractor
