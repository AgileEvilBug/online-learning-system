# users/management/commands/resetdb.py
from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = "Resets the database by flushing and re-running migrations."

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING("Flushing database..."))
        call_command("flush", interactive=False)

        self.stdout.write(self.style.WARNING("Running migrations..."))
        call_command("migrate")

        self.stdout.write(self.style.SUCCESS("Database has been reset!"))
