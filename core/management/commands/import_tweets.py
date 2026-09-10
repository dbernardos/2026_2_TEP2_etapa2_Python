import csv
from django.core.management.base import BaseCommand
from core.models import Tweet

class Command(BaseCommand):
    help = 'Importa tweets do dataset CSV para o banco de dados do Django'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Caminho para o arquivo CSV')

    def handle(self, *args, **kwargs):
        csv_file_path = kwargs['csv_file']

        self.stdout.write(self.style.SUCCESS(f'Iniciando importação do arquivo: {csv_file_path}'))
        tweets_to_create = []

        try:
            with open(csv_file_path, mode='r', encoding='utf-8-sig') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    keyword = row['keyword'] if row['keyword'] else None
                    location = row['location'] if row['location'] else None
                    tweet = Tweet(
                        id=int(row['id']),
                        keyword=keyword,
                        location=location,
                        text=row['text'],
                        target=int(row['target'])
                    )
                
                    tweets_to_create.append(tweet)
            Tweet.objects.bulk_create(tweets_to_create, batch_size=1000)
            self.stdout.write(self.style.SUCCESS(f'Sucesso! {len(tweets_to_create)} tweets importados.'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'Erro: Arquivo não encontrado em {csv_file_path}'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Ocorreu um erro durante a importação: {str(e)}'))