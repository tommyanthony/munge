# munge
A command line tool for converting data from one type to another. This is useful for data science when one has many types of data in different formats, and can be quickly converted to the same data type with munge!

## Installation
If you want to contribute
```shell
git clone https://github.com/tommyanthony/munge
cd munge
pip install --editable ./
pip install -r requirements.txt
```

Otherwise to simply use munge
```
git clone https://github.com/tommyanthony/munge
cd munge
pip install --editable ./
```
## Usage
All the following examples use the data from the test-data directory, so follow along!
```shell
> ls
github.csv      in.json         out.html
in.csv          in.xlsx         presidents.yaml
> cat in.json
[
  {
    "last_name": "Adams",
    "age": 90,
    "first_name": "John"
  },
  {
    "last_name": "Ford",
    "age": 83,
    "first_name": "Henry"
  }
]
> munge csv -i in.json
first_name,age,last_name
John,90,Adams
Henry,83,Ford

> cat presidents.yaml
- {first_name: John, last_name: Adams}
- {first_name: George, last_name: Washington}

> munge -i presidents.yaml csv
last_name,first_name
Adams,John
Washington,George

> munge -i in.csv -o output.json json
> cat output.json
[{"first_name": "John", "last_name": "Adams"}, {"first_name": "George", "last_name": "Washington"}]
```
Munge by default reads from standard in and prints to stdout, allowing it to interact with all the other UNIX utilities you're used to.
```shell
> curl https://raw.githubusercontent.com/rankam/napoleon/ce658a0ff1a16debc240a6c9b3790ac1b9a8efd5/original_data/cities.json | munge csv -o cities.csv
> cat cities.csv
cities_lat,cities_long,cities_city
55,24,Kowno
54.7,25.3,Wilna
54.4,26.4,Smorgoni
54.3,26.8,Moiodexno
55.2,27.7,Gloubokoe
...
```

## In development
I'm currently working on the ability to perform transforms on the dataset in munge, and development for this can be seen under transforms branch.
