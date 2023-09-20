def execute_command(command):
    if command == 'ls':
        print('$ listing files')
    elif command == 'cd':
        print('$ changing directory')
    else:
        print('$ no commands')

    print('...... ')

def execute_commands(command:str):
    match command: #match é o switch
        case 'ls':
            print('$ listing files')
        case 'cd':
            print('$ changing directory')
        case _: # _ é o default
            print('$ no commands')

    print('...... ')

execute_command('cd')
execute_commands('cds')

@dataclass
class Command:
    command:str
    directories:list[str]

def commands_on_switch(command):
    match command.split():  #recebendo o valor após modificar a str
    # a ordem dos cases afeta o produto
        case ['cd']:
            print('$ changing directory to',path)

        case ['cd' | 'lss']: #dizendo que pode ser ou esse valor ou o outro
            print('$ changing directory to',path)

        case ['cd' | 'lss'] | ['cdd']: #dizendo que pode ser ou esse valor ou o outro, pode ser criados novos arrays tambem
            print('$ changing directory to',path)

        case ['cd', path]:#como voce fez o split o valor virou basicamente um array,o path basicamente vai virar o segundo valor do split da string se tornando uma variavel dinamica
            print('$ changing directory to',path)

        case ['ls', path, path_um, path_dois]: #mais de um valor passado 
            print('$ files from path', path)

        case ['ls', path, *_]: #empacotando tudo o que foi passado depois com *
            print('$ files from path', path)

        case ['cd' | 'lss', path] if len(path) <= 1: #criando condicionais dentro dos cases, assim ele tem que passar pelo case and pelo if
            print('$ changing directory to',path)

        case ['cd' | 'lss', path] if len(path) > 1: #criando condicionais dentro dos cases
            print('$ changing more to',path)


        case ['ls', *directories]: #empacotando tudo o que foi passado com *
            for directory in directories:   #listando tudo que foi empacotado
                print('$ files from path', directory)

        case ['cd' | 'lss' as commands,*directories] as lists if len(directories) > 1: # as é usado como uma nomeação para acesso rapido as variaveis
            for directory in directories:   #listando tudo que foi empacotado
                print('$ files from path', directory)
            print(f'{commands=}, {lists=}') #utilizando o alias

        case ['ls', *directories, '--force']: #empacotando tudo o que foi passado com *, e dizendo que caso tenha --force no final roda isso
            for directory in directories:   #listando tudo que foi empacotado
                print('$ files from path', directory)

        case ['ls', *directories, '--force', _]: #empacotando tudo o que foi passado com *, e dizendo que caso tenha --force no final roda isso, e criando _ como variavel generica
            for directory in directories:   #listando tudo que foi empacotado
                print('$ files from path', directory)

        case ['cd', 'ark']:
            print('$ changing directory to',path)

        case {'command':'ls'}: #utilizando dicionarios, ele verifica se no dicionario tem o itens do case
            for directory in command['command']:
                print('$ listing directories ',directory)

        case {'command':'ls','directories':[]}: #utilizando dicionarios, ele verifica se no dicionario tem os dois itens do case, porem a chave sendo uma lista vazia
            for directory in command['directories']:
                print('$ listing directories ',directory)

        case {'command':'ls','directories':[_]}: #utilizando dicionarios, ele verifica se no dicionario tem os dois itens do case, porem a chave sendo uma lista com um item
            for directory in command['directories']:
                print('$ listing directories ',directory)

        case {'command':'ls','directories':[_,*_]}: #utilizando dicionarios, ele verifica se no dicionario tem os dois itens do case, porem a chave sendo uma lista com um item ou varios elementos
            for directory in command['directories']:
                print('$ listing directories ',directory)

        case {'command':'ls','directories':[*_]}: #utilizando dicionarios, ele verifica se no dicionario tem os dois itens do case, porem a chave sendo uma lista com varios elementos ou nenhum
            for directory in command['directories']:
                print('$ listing directories ',directory)

        case Command(command='ls'): #utilizando classes para entrar nos resultados
            print("entrou no objeto")

        case Command(command=_,directories=[_,*_]): #utilizando classes para entrar nos resultados, o _ significa um objeto generico podendo ser qualquer coisa, por isso a ordem dos cases é importante
            for directory in command.directories:
                print('$ listing directories ',directory)

        case Command(command='ls',directories=[_,*_]): #utilizando classes para entrar nos resultados
            for directory in command.directories:
                print('$ listing directories ',directory)

        case _:
            print('$ no commands')

    print(command.split())
    print(command.split(','))



commands_on_switch("ls value")
commands_on_switch({'command':'ls','directories':[]})


