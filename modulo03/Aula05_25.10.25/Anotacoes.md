# Automatiza que Cresce

- Testes unitários
- Documentação técnica
- Versionamento
- Implementação de testes unitários para APIs REST

<br>

## Por que testar?
O custo de um código não testado resulta em retrabalho, falhas e atrasos no desenvolvimento,

### Com testes, a expectativa é:
1. Bugs são detectados antes da produção;
2. Confiança para refator (_um código testado é um código documentado_);
3. Documentação viva do código;
4. Menos estresse, mais qualidade, isto é. menos fricção no processo de desenvolvimento.

**OBS.:** não devem ser lentos, nem pesar. Precisam ser simples e objetivos.

<br>

### Pirâmide de Testes

```bash
            _
           / \
          /E2E\            Testes end-to-end: pouco utilizados, lentos.    
         /_____\
        /       \
       / INTEGRA \         Testes de integração: alguma utilização, velocidade média. 
      /___________\
     /             \
    /   UNITÁRIOS   \      Testes unitários: muito utilizados, rápidos. 
   /_________________\
```

#### Regra de Ouro
- 70% Unitários: normalmente para regras de neócios
- 20% Integração
- 10% E2E

<br>

### Testando com Python
#### Pytest

- instalando
```bash
pip install pytest pytest-cov
pip install flask #ou fastapi
```

<br>

- estrutura de diretórios
```bash
meu_projeto/
    app/
        main.py
        routes.py
    tests/
        conftest.py
        test_routes.py
    requirements.py
```
_Poderá variar de acordo com a padronização da cia_


#### Exemplo de API
API de usuários - código base
```py
# app/main.py
from flask import Flask, jsonify, request

app = Flask(__name__)

usuarios = []

@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    return jsonify(usuarios), 200

@app.route('/usuarios', methods=['POST'])
def criar_usuario():
    dados = request.get_json()
    
    if not dados or 'nome' not in dados:
        return jsonify({"erro": "Nome é obrigatório"}), 422 # 422 Unprocessable Entity | o servidor entendeu a sua solicitação (JSON/XML, etc.), mas não pôde processá-la devido a erros semânticos nos dados
    
    usuario = {
        "id": len(usuarios) + 1,
        "nome": dados['nome'],
        "email": dados.get('email', '')
    }
    
    usuarios.append(usuario)
    return jsonify(usuario), 201 # significa "Created" (Criado) | criação bem-sucedida de um ou mais recursos

@app.route('/usuarios/<int:user_id>', methods=['GET'])
def buscar_usuario(user_id):
    usuario = next((u for u in usuarios if u['id'] == user_id), None)
    
    if not usuario:
        return jsonify({"erro": "Usuário não encontrado"}), 404
    
    return jsonify(usuario), 200

if __name__ == '__main__':
    app.run(debug=True)
```

<br>

### Configurando Fixtures
`conftest.py` - setup de testes

#### O que são Fixtures?
- Enviam código duplicado
- Funções de setup reutilizáveis
- Executam antes/depois dos testes

#### Exemplo de código
```py
# tests/conftest.py
import pytest
from app.main import app

@pytest.fixture
def client():
    """Cria um cliente de teste para a aplicação Flask"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
    
    # Limpeza: resetar lista de usuários após cada teste
    from app.main import usuarios
    usuarios.clear() 
```

#### Exemplos de Testes
- Teste Simples
```py
def test_buscar_usuario_inexistente(client):
    """Testa busca de usuário que não existe"""
    response = client.get('/usuarios/999')
    
    assert response.status_code == 404
    assert "erro" in response.json
```

- Teste com POST
```py
def test_buscar_usuario_existente(client):
    """Testa busca de usuário que existe"""
    # Arrange: criar um usuário primeiro
    novo_usuario = {"nome": "Carlos", "email": "carlos@example.com"}
    response_criacao = client.post(
        '/usuarios',
        data=json.dumps(novo_usuario),
        content_type='application/json'
    )
    user_id = response_criacao.json['id']
    
    # Act: buscar o usuário
    response = client.get(f'/usuarios/{user_id}')
    
    # Assert: verificar resposta
    assert response.status_code == 200
    assert response.json['nome'] == "Carlos"
```

- Teste de erro (uma espécie de TDD)
```py
def test_criar_usuario_sem_nome(client):
    """Testa validação quando nome não é fornecido"""
    usuario_invalido = {"email": "teste@example.com"}
    
    response = client.post(
        '/usuarios',
        data=json.dumps(usuario_invalido),
        content_type='application/json'
    )
    
    assert response.status_code == 400
    assert "erro" in response.json
    assert "obrigatório" in response.json["erro"].lower()
```
***Testar cenários de erro é tão importante quanto testar sucesso!***

<br>

### Padrão AAA
**A**rrange, **A**ct, **A**sert

#### Benefícios do Padrão
- Estrutura clara;
- Fácil manutenção;
- Testes mais legíveis.

#### Exemplo
```py
def test_buscar_usuario_existente(client):
    """Testa busca de usuário que existe"""
    # Arrange: criar um usuário primeiro (preparação)
    novo_usuario = {"nome": "Carlos", "email": "carlos@example.com"}
    response_criacao = client.post(
        '/usuarios',
        data=json.dumps(novo_usuario),
        content_type='application/json'
    )
    user_id = response_criacao.json['id']
    
    # Act: buscar o usuário (execução)
    response = client.get(f'/usuarios/{user_id}')
    
    # Assert: verificar resposta (verificação)
    assert response.status_code == 200
    assert response.json['nome'] == "Carlos"
```

<br>

**OBS**.: No VS Code há a extensão Python Test Explorer
- Comandos Pytest
```bash
# No terminal integrado do VSCode
pytest

# Com informações detalhadas
pytest -v

# Com cobertura de código
pytest --cov=app --cov-report=html

# Executar apenas um arquivo
pytest tests/test_routes.py

# Executar apenas um teste específico
pytest tests/test_routes.py::test_criar_usuario_sucesso
```

<br>

### Boas práticas de código
#### Como escrever bons testes?

**Faça**                       | **Não Faça**
------------------------------ | ----------------------------
Nomes descritivos              | Ignorar cenários de erro
Testes independes              | Lógica complexa nos testes
Use fixtures para reutilização | Testar implementação interna
Um teste = uma funcionalidade  | Testes que dependem de ordem

<br>

## Documentação Técnica
### A importância da documentação
Sem documentação                | Com documentação
------------------------------- | -------------------
"Como executar este projeto?"   | Autodescritivo
" O que este endpoint faz?"     | Onboarding rápido
" Quais são as dependências?"   | Reduz interrupções
Outros desenvolvedores perdidos | Projeto profissional

_**LEMBRE-SE:** Você no futuro é "outro desenvolvedor"!_

### README.md

