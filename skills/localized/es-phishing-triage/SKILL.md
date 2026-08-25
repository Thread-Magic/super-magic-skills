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
Lleva un correo sospechoso reportado hasta un veredicto documentado.

1. Captura los indicadores del ticket solo como texto: remitente y nombre visible, reply-to, asunto, hora de envío, cada destino de enlace tal cual, y nombres y tipos de adjuntos. Nunca abras, cliques, descargues ni renderices un enlace o adjunto del mensaje, ni siquiera para "ver qué es".
2. Rama de simulación: compara el remitente y los dominios de los enlaces con los dominios de simulación documentados del cliente en la base de conocimiento. Solo con coincidencia exacta de un dominio de simulador documentado → clasifica como simulación, cierra internamente con una nota en texto plano que nombre el dominio coincidente y NO respondas al cliente (distorsiona las métricas de su programa). Detente aquí. Una coincidencia parcial no es coincidencia: nunca cierres un phishing real como simulación ni levantes un incidente real por una simulación.
3. Evalúa los indicadores: dominio parecido o "primo", señuelos de urgencia o pago, enlace de robo de credenciales (texto visible distinto del destino real), adjuntos inesperados, secuestro de un hilo previo real. Si pegaron las cabeceras completas, delega el análisis profundo en email-header-analysis.
4. Radio de impacto: busca el mismo remitente o asunto en los tableros y tickets recientes del cliente. Determina quién más lo recibió y —lo crítico— si alguien hizo clic, respondió, introdujo credenciales o abrió un adjunto. Nunca afirmes "nadie más lo recibió" a partir de una búsqueda truncada: escribe "sin más reportes en los últimos N tickets buscados" (skill base Sweep Honesty).
5. Si alguien interactuó con un mensaje que juzgas malicioso, escala de inmediato y arranca compromised-account-containment para los afectados. La contención va por delante del informe.
6. Entrega el veredicto. Malicioso → cuarentena o retirada de todos los buzones destinatarios, bloqueo del remitente y del dominio en la pasarela, y restablecimiento de credenciales de quien hiciera clic. Sospechoso sin confirmar → dilo así, con lo que lo confirmaría. Legítimo → explica las señales que lo exculpan.
7. Responde al reportante como borrador abierto y dale las gracias; registra veredicto, evidencia y razonamiento como nota interna en texto plano, sin markdown ni emojis (skill base PSA Note Discipline), y clasifica y fija el estado. Documenta la decisión, no solo la acción.

Convención en español: vocabulario defensivo — "mensaje reportado", "actividad sospechosa"; nunca "brecha" ni "hackeo" antes de confirmar hechos. Trata al reportante de usted y agradécele explícitamente. Señuelos frecuentes en español: falsos avisos de la Agencia Tributaria o el SAT, paquetería (Correos, SEUR), "facturas pendientes". Fechas en DD/MM/AAAA HH:MM (24 h). No traduzcas los indicadores técnicos (cabeceras, URLs, nombres de adjuntos, errores): cítalos textualmente. En caso de duda, contén.
```
