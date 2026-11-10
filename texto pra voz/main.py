import pyttsx3


def inicializar_motor():
  engine = pyttsx3.init()
  return engine


def falar_texto():
  engine = inicializar_motor()

  print("=== Gerador de Voz Simples com pyttsx3 ===")

  # 1. Entrada do texto
  texto = input("\nDigite o que você quer que a voz diga: ")

  # 2. Escolha da velocidade (Rate)
  print("\n--- Velocidade da Voz ---")
  try:
    velocidade = int(
        input("Digite a velocidade (ex: 100 para lento, 200 para normal): ")
    )
  except ValueError:
    velocidade = 200
  engine.setProperty('rate', velocidade)

  # 3. Escolha da voz (Tom / Gênero / Idioma)
  voices = engine.getProperty('voices')

  print(f"\n--- Vozes Disponíveis no seu Computador ({len(voices)}) ---")
  for index, voice in enumerate(voices):
    print(f"[{index}] Nome: {voice.name}")

  print("\n💡 QUER MAIS VOZES? (Português do Brasil natural, etc.)")
  print(
      "• Baixe pelo Windows: Configurações > Hora e Idioma > Fala > Adicionar"
      " vozes."
  )
  print("• Site para baixar pacotes de voz (SAPI5/TTS):")
  print(
      "  🔗 https://www.appy-geek.com (ou pesquise por 'Microsoft Speech Platform"
      " Runtime e Language Packs')"
  )
  print(
      "⭐ Recomendadas: Procure pelos pacotes de voz em Português do Brasil"
      " (ex: 'Microsoft Maria' ou pacotes SAPI5 compatíveis com pyttsx3)."
  )

  try:
    escolha_input = input(
        "\nEscolha o número da voz desejada (ou aperte Enter para usar a"
        " padrão): "
    )
    if escolha_input.strip() == "":
      print("Usando a voz padrão.")
    else:
      escolha_voz = int(escolha_input)
      if 0 <= escolha_voz < len(voices):
        engine.setProperty('voice', voices[escolha_voz].id)
      else:
        print("Opção inválida. Usando a voz padrão.")
  except ValueError:
    print("Entrada inválida. Usando a voz padrão.")

  # 4. Executando a fala
  print("\n🔊 Reproduzindo áudio...")
  engine.say(texto)
  engine.runAndWait()
  print("✅ Finalizado!")


if __name__ == "__main__":
  falar_texto()
