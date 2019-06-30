#!/usr/bin/env python2.7

import dbmanager


def run():
    """ Start the reporting tool """
    question_1()

    print "\n"
    question_2()

    print "\n"
    question_3()


def question_1():
    print "Q1. What are the most popular three articles of all time?\n"
    rows = dbmanager.get_most_popular_articles()
    for row in rows:
        print "\t%s - %d views" % (row[0], row[1])


def question_2():
    print "Q2. Who are the most popular article authors of all time?\n"
    rows = dbmanager.get_most_popular_authors()
    for row in rows:
        print "\t%s - %d views" % (row[0], row[1])


def question_3():
    print "Q3. On which days did more than 1% of requests lead to errors?\n"
    rows = dbmanager.get_days_with_more_errors()
    for row in rows:
        print "\t%s - %s errors" % (row[0], row[1])


run()
