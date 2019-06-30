# Logs Analysis

The objective of the Logs Analysis Project is to create a reporting tool that prints out reports based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.


## How to run this?

### 1. Setup:

**Step 1:**  Download the database dump from [this link](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).

Then, copy the database dump `newsdata.sql` to the `vagrant/`.

**Step 2:** Open the terminal. Then, run the following commands:

```
# Install & Configure VM
cd /path/to/vagrant
vagrant up

# Log into machine
vagrant ssh

# Populate database using dump in shared folder 
cd /vagrant 
psql -d news -f newsdata.sql

```

### 2. Run the Reporting Tool

Open the terminal. Then, run the following commands:

```
# Run the program
python reportool.py
```

## Questions to answer

The reporting tool will answer the following questions

**(1) What are the most popular three articles of all time?**

Example:

- "Princess Shellfish Marries Prince Handsome" — 1201 views
- "Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views
- "Political Scandal Ends In Political Scandal" — 553 views

**(2) Who are the most popular article authors of all time?***

Example:

- Ursula La Multa — 2304 views
- Rudolf von Treppenwitz — 1985 views
- Markoff Chaney — 1723 views
- Anonymous Contributor — 1023 views



**(3) On which days did more than 1% of requests lead to errors?**

Example:

- July 29, 2016 — 2.5% errors