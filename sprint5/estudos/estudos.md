# Amazon Web Services - AWS

## AWS ou serviços On-Premises?

### Benefícios AWS:

1. **Escalabilidade**: Permite aumentar ou diminuir a capacidade de computação de forma rápida e fácil conforme a demanda.
2. **Custos Flexíveis**: Modelo de pagamento conforme o uso (pay-as-you-go), eliminando grandes investimentos iniciais.
3. **Disponibilidade Global**: Alta disponibilidade, com data centers em várias regiões do mundo.
4. **Ampla Gama de Serviços**: Oferece uma vasta gama de serviços, desde computação, armazenamento, bancos de dados, até ferramentas de inteligência artificial e aprendizado de máquina.
5. **Segurança**: Elevados padrões de segurança com certificações de conformidade, criptografia de dados e monitoramento contínuo.

#### Benefícios On-Premises:

1. **Controle Total**: Total controle sobre a infraestrutura física e os dados.
2. **Segurança**: Maior controle sobre a segurança física e lógica dos servidores.
3. **Latência**: Menor latência para aplicações locais.
4. **Conformidade**: Facilita a conformidade com regulamentos específicos que exigem dados localizados fisicamente (LGPD?).

A depender do caso, pode-se optar por uma gestão **híbrida**, que oferece flexibilidade e otimização de custos, mas pode ser mais complexa de gerenciar e integrar, além de ter custos iniciais mais elevados nesses pontos.

## EC2 - Elastic Compute Cloud

Computação redimensionável - Maior **flexibilidade** e fácil **escalabilidade** das aplicações WEB.

### Uso Comum do Amazon EC2

* Hospedagem de sites e aplicações web.
* Execução de ambientes de desenvolvimento e teste.
* Processamento de grandes volumes de dados e análises.
* Implementação de aplicativos empresariais.
* Execução de workloads críticos que requerem alta disponibilidade e segurança.

### Availability Zones

Dentro de cada **Região** geográfica, existem as **Zonas de Disponibilidade** (Availability Zones), ou seja, os data centers isolados fisicamente dentro de cada região. Esses servidores podem ser usados como backup, por exemplo. Isso permite disponibilidade e redundância dentro de uma mesma região, mantendo também a baixa latência, uma vez que os servidores de backup ainda estarão na mesma região.

![Amazon Regions and AZs](https://media.geeksforgeeks.org/wp-content/uploads/20230802125628/AWS-EC2-Instance-types.png)

## VPCs - Virtual Private Cloud

Permite isolar seções da nuvem AWS, ativando recursos em uma rede virtual que você define. A VPC fornece controle total sobre o ambiente de rede, incluindo IP, criação de sub-redes, configuração de tabelas de roteamento e gateways de rede.

Permite um eficaz **isolamento de instâncias e seus serviços**, controlando também a forma como eles se comunicam.

![VPCs](https://docs.aws.amazon.com/pt_br/vpc/latest/userguide/images/how-it-works.png)

A comunicação entre redes é feita através do processo de **VPC Peering (Emparelhamento de redes VPC)**. Nesse processo, as tabelas de endereços e as restrições de segurança devem ser alterados para garantir o funcionamento.

## Auto Scaling e Load Balancer

Os recursos EC2 da AWS também contam com escalamento e diminuições programadas, e com balanceamento de carga.


## S3 e Buckets

**S3 (Simple Storage Service)** \- Serviço de **armazenamento** de objetos.

Um **bucket** é um contêiner dentro do Amazon S3 que armazena objetos, que podem ser arquivos de qualquer tipo (imagens, vídeos, documentos, backups, etc.). Cada bucket é identificado de forma única dentro da AWS e serve como o ponto de partida para armazenar e organizar dados.

Pode-se usar o bucket também para hospedar **arquivos estáticos**, sejam eles sites, JSON, e outros arquivos em geral.

![Amazon S3](https://d1.awsstatic.com/s3-pdp-redesign/product-page-diagram_Amazon-S3_HIW@2x.ee85671fe5c9ccc2ee5c5352a769d7b03d7c0f16.png)

## EFS Elastic File System

Sistema de armazanamento escalável de arquivos. Ideal para instâncias AWS trabalharem entre si, diferente do s3(Buckets), onde o foco é disponibilidade WEB.

## Bancos de Dados

### RDS - Relational Database Services

Serviço automatiazado de manutenção e gerenciamento de DBs, que trabalha com Availability Zones e permite crias as chamadas **Read Replicas**, cópias dos bancos que só permitem leitura, mas são mais rápidas em situações de alto consumo e sobrecarga.

### Dynamo DB

Serviço para criar bancos de dados flexíveis (não-relacional) na AWS.

## IAM - Identity and Acess Management

Recurso para gerenciar usuários, grupos e permissões na AWS.

## AWS Pricing Calculator

Ferramenta que permite estimar o preço de uma migração para AWS EC2, a partir das prováveis demandas dos clientes (hardware, armazenamento, número de servidores, tipo de serviço, entre outros). **Facilita a migração e a visualização da economia de custos.**

OBS:. Custo não é a única vantagem da AWS, mas é a vantagem que os clientes mais querem ver inicialmente. Talvez a economia de custos venha a médio ou longo prazo, a depender de cada aplicação.