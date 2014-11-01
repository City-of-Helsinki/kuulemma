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

2. Install Python dependencies::

    $ pip install -r requirements-dev.txt

3. Create databases for development and testing::

    $ createdb kuulemma
    $ createdb kuulemma_test

4. Create database tables::

    $ alembic upgrade head

5. Install npm dependencies::

    $ npm install

6. Install bower dependencies::

    $ bower install

7. Finally, start the development server::

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
