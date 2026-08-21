---
name: Triaje de phishing (Spanish)
description: Triaje de phishing de un correo sospechoso: evaluar sin tocar la carga, medir radio de impacto, contener si es malicioso y responder al reportante.
category: Localized
tools: [search_tickets, search_contacts, search_knowledge_base, add_ticket_note, update_ticket, view_openDraft]
connectors: []
scope: single
flow: no
role: [Security & Compliance Owner]
outcome: [Risk & Compliance]
---

# Triaje de phishing (Spanish)

**Cuándo usar:** un usuario reenvió algo sospechoso ("¿esto es phishing?"), un ticket de reporte cae en el tablero de seguridad, o un técnico quiere una segunda opinión antes de liberar o borrar un mensaje.

**Ejecutar:** sobre un único mensaje reportado.

## Prompt

```
Lleva este correo sospechoso reportado hasta un veredicto documentado.

1. Captura los indicadores del ticket sin interactuar con ellos: dirección y nombre visible del remitente, reply-to, asunto, hora de envío, cada destino de enlace exactamente como está escrito, y nombres y tipos de los adjuntos. Nunca abras enlaces ni adjuntos, y nunca visites una URL del mensaje para "ver qué es".
2. Rama de simulación: compara el remitente y los dominios de los enlaces con los dominios documentados de la plataforma de simulación de phishing del cliente (busca en la base de conocimiento la ficha del proveedor de simulación). Si coincide con un simulador conocido → clasifica como simulación, cierra internamente con una nota en texto plano que nombre el dominio casado, y NO respondas al cliente (una respuesta distorsiona las métricas de su programa de simulación). Detente aquí.
3. Evalúa los indicadores: dominio parecido o "primo", señuelos de urgencia y pagos, enlace de robo de credenciales (texto visible frente a destino real discrepantes), tipos de adjunto inesperados, secuestro de un hilo real previo. Si pegaron las cabeceras completas, delega el análisis profundo en la skill email-header-analysis e incorpora su veredicto.
4. Comprobación de radio de impacto: busca el mismo remitente o asunto en los tableros del cliente y los tickets recientes. Determina quién más recibió el mensaje y — lo crítico — si alguien hizo clic, respondió, introdujo credenciales o abrió un adjunto (identifica a los destinatarios en la lista de contactos).
5. Si alguien interactuó con un mensaje que juzgas malicioso → escala de inmediato y arranca la skill compromised-account-containment para los usuarios afectados. La contención va por delante de terminar el informe: contén rápido, investiga después.
6. Entrega el veredicto: Malicioso → recomienda cuarentena/retirada de todos los buzones destinatarios, bloqueo del remitente/dominio en la pasarela y restablecimiento de credenciales para quien hiciera clic. Sospechoso sin confirmar → dilo exactamente así, indicando qué lo confirmaría. Legítimo → explica las señales que lo exculpan.
7. Responde al reportante como borrador abierto usando el vocabulario de redacción defensiva (un correo sospechoso es un "mensaje reportado", no una "brecha"). Registra el veredicto, la evidencia y el razonamiento como nota interna; clasifica y fija el estado del ticket. Agradece al reportante.

Convención en español: vocabulario defensivo — "mensaje reportado", "actividad sospechosa", "indicios de suplantación"; nunca "brecha", "hackeo" ni "estamos comprometidos" antes de confirmar hechos. Respuesta al reportante en registro de usted y con agradecimiento explícito: "Gracias por reportarlo; es exactamente lo que debemos hacer con los correos sospechosos." Reconoce señuelos frecuentes en campañas en español: falsas notificaciones de la Agencia Tributaria/SAT, avisos de paquetería (Correos, SEUR), "facturas pendientes". Marca de tiempo del veredicto en DD/MM/AAAA HH:MM (24 h). No traduzcas los indicadores técnicos (cabeceras From/Reply-To/Return-Path, URLs, nombres de adjuntos, mensajes de error): cítalos textualmente en su idioma original.

Salvaguardas: nunca abras, cliques, descargues ni renderices enlaces o adjuntos del mensaje reportado — captura los indicadores solo como texto. Comprueba la simulación en ambos sentidos (nunca levantes un incidente real por una simulación; nunca cierres un phishing real como simulación por una coincidencia parcial de dominio — exige un dominio de simulador documentado y exacto). Nunca respondas al cliente sobre una simulación confirmada. Clic o respuesta significa escalar de inmediato. Nunca afirmes "nadie más lo recibió" a partir de una búsqueda truncada; informa "sin más reportes encontrados en los últimos N tickets buscados". Documenta la decisión, no solo la acción. En caso de duda, contén.
```
