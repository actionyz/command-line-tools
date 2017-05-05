import click
import requests
import request
from tqdm import *
from time import sleep
@click.group()
def cli():
    click.secho('Begain',fg='black')

#
@cli.command()
@click.option('--count', help='Number of greetings.',prompt='input argvs')
def initdb(count):
    click.echo(count)

@cli.command()
@click.option('--count', help='Number of greetings.')
def dropdb(count):
    click.echo('Dropped the database'+count)

@cli.command()
@click.option('--url', help='The target url')
@click.option('--count', default=10 ,help='The number of thread you want')
def find(url,count):
	
	#read file try to request url in dic 
	request.thread(url,10)
	# lists =[]
	# f = open('../docs/dic','r')
	# f_list = f.readlines()
	# pbar = tqdm(f_list)
	# for f_list in pbar: 
	# 	urls = url+'/'+f_list[:-1]
	# 	s = request.request(urls)
	# 	if s != 404:
	# 		lists.append(urls+' '+str(s))		
		
	for i in request.lists:
	 	click.secho(i,fg='green')

if __name__ == '__main__':
	cli()