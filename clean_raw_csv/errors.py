class InvalidProcessTechnique(Exception):
    def __str__(self):
        return 'The process key you specified is invalid'

