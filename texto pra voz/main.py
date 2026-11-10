import pyttsx3


def inicializar_motor():
  # Inicializa o mecanismo de conversão de texto em fala
  engine = pyttsx3.init()
  return engine


def falar_texto():
  engine = inicializar_motor()

  print("=== Gerador de Voz Simples com pyttsx3 ===")

  # 1. Entrada do texto
  texto = input("\nDigite o que você quer que a voz diga: ")

  # 2. Escolha da velocidade (Rate)
  print("\n--- Velocidade da Voz ---")
  print("Padrão costuma ser em torno de 200.")
  try:
    velocidade = int(
        input("Digite a velocidade (ex: 100 para lento, 200 para normal): ")
    )
  except ValueError:
    velocidade = 200  # Valor padrão se o usuário digitar algo errado
  engine.setProperty('rate', velocidade)

  # 3. Escolha da voz (Tom / Gênero / Idioma)
  voices = engine.getProperty('voices')
  print(f"\n--- Vozes Disponíveis ({len(voices)} encontradas) ---")
  for index, voice in enumerate(voices):
    print(f"[{index}] Nome: {voice.name} | Idioma: {voice.languages}")

  try:
    escolha_voz = int(input("Escolha o número da voz desejada: "))
    if 0 <= escolha_voz < len(voices):
      engine.setProperty('voice', voices[escolha_voz].id)
    else:
      print("Opção inválida. Usando a voz padrão.")
  except ValueError:
    print("Entrada inválida. Usando a voz padrão.")

  # 4. Executando a fala
  print("\nReproduzindo áudio...")
  engine.say(texto)
  engine.runAndWait()
  print("Finalizado!")


if __name__ == "__main__":
  falar_texto()