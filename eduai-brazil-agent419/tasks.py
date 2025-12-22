"""Edu.AI Brazil Tasks"""

from crewai import Task
from agents import brazil_curriculum_specialist, portuguese_content_creator, enem_prep_specialist, inclusive_education_advisor, assessment_creator_br


def create_tasks(course_info: dict):
    """Create Brazilian education tasks"""

    subject = course_info.get('subject', 'Matemática')
    level = course_info.get('level', 'Ensino Fundamental')

    curriculum_task = Task(
        description=f"""Criar currículo para {subject} - {level} alinhado com BNCC.

        Desenvolver:
        1. Objetivos de aprendizagem (competências BNCC)
        2. Habilidades específicas
        3. Estrutura de módulos
        4. Progressão pedagógica
        5. Conexões interdisciplinares""",
        agent=brazil_curriculum_specialist,
        expected_output="Currículo completo alinhado com BNCC"
    )

    content_task = Task(
        description=f"""Criar conteúdo educacional em português para {subject}.

        Incluir:
        1. Explicações claras em português brasileiro
        2. Exemplos do contexto brasileiro
        3. Atividades práticas
        4. Recursos multimídia
        5. Materiais de apoio""",
        agent=portuguese_content_creator,
        expected_output="Conteúdo educacional completo em português",
        context=[curriculum_task]
    )

    enem_task = Task(
        description=f"""Criar materiais de preparação para ENEM - {subject}.

        Desenvolver:
        1. Questões estilo ENEM
        2. Simulados
        3. Estratégias de resolução
        4. Cronograma de estudos
        5. Dicas para o dia da prova""",
        agent=enem_prep_specialist,
        expected_output="Material completo de preparação ENEM",
        context=[curriculum_task, content_task]
    )

    inclusive_task = Task(
        description=f"""Revisar materiais para inclusão e acessibilidade.

        Verificar:
        1. Acessibilidade para estudantes com deficiências
        2. Adaptação para diferentes contextos socioeconômicos
        3. Consideração de diversidade regional brasileira
        4. Linguagem inclusiva
        5. Recursos para aprendizagem diferenciada""",
        agent=inclusive_education_advisor,
        expected_output="Relatório de inclusão com recomendações",
        context=[curriculum_task, content_task]
    )

    assessment_task = Task(
        description=f"""Criar avaliações para {subject} - {level}.

        Desenvolver:
        1. Avaliações diagnósticas
        2. Avaliações formativas
        3. Avaliações somativas
        4. Rubricas de correção
        5. Banco de questões""",
        agent=assessment_creator_br,
        expected_output="Sistema completo de avaliação",
        context=[curriculum_task, content_task, enem_task, inclusive_task]
    )

    return [curriculum_task, content_task, enem_task, inclusive_task, assessment_task]
