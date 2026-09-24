import flet as ft
from google import genai

client = genai.Client()

def main(page: ft.Page):

    # -----------------------------
    # PAGE SETTINGS
    # -----------------------------

    page.title = "GreenGuide"
    page.bgcolor = "#F7FAF8"
    page.padding = 0

    # -----------------------------
    # AI INPUT
    # -----------------------------

    question = ft.TextField(
        hint_text="Ask something about the environment...",
        color=ft.Colors.BLACK,
        expand=True,
    )

    # This will display the AI answer later
    answer = ft.Text(
        "AI's answer will appear here.",
        color="#064E3B",
    )

    def ask_ai(e):
        question_text = question.value

        if not question_text:
            answer.value = "Please enter a question."
            page.update()
            return

        try:
            response = client.models.generate_content(
                model="gemini-3.8-flash",
                contents = f"""
                    You are GreenGuide, a simple environmental assistant.

                    Give short, practical and easy-to-understand advice.

                    User's question:
                    {question_text}
                    """,
            )

            answer.value = response.text

        except Exception as error:
            answer.value = f"Error: {error}"

        page.update()

    # -----------------------------
    # HEADER
    # -----------------------------

    header = ft.Container(
        content=ft.Row(
            controls=[
                ft.Text(
                    "🌿 GreenGuide",
                    size=24,
                    weight=ft.FontWeight.BOLD,
                    color="#064E3B",
                ),

                ft.Row(
                    controls=[
                        ft.TextButton(content="Home"),
                        ft.TextButton(content="About"),
                    ],
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        padding=ft.Padding.symmetric(
            horizontal=40,
            vertical=15,
        ),
        bgcolor="#FFFFFF",
    )

    # -----------------------------
    # HERO
    # -----------------------------

    hero = ft.Container(
        content=ft.Row(
            controls=[
                ft.Column(
                    controls=[
                        ft.Text(
                            "Make greener choices.",
                            size=38,
                            weight=ft.FontWeight.BOLD,
                            color="#064E3B",
                        ),

                        ft.Text(
                            "Get simple advice with AI.",
                            size=18,
                            color="#66736B",
                        ),

                        ft.Button(
                            content="Get Started",
                            on_click=ask_ai,
                        ),
                    ],
                    spacing=10,
                ),

                ft.Text(
                    "🌍",
                    size=80,
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        padding=ft.Padding.symmetric(
            horizontal=60,
            vertical=45,
        ),
        bgcolor="#E8F5EE",
    )

    # -----------------------------
    # AI SECTION
    # -----------------------------

    ai_section = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text(
                    "✨ Ask GreenGuide",
                    size=26,
                    weight=ft.FontWeight.BOLD,
                    color="#064E3B",
                ),

                ft.Text(
                    "Ask a question and get helpful environmental advice.",
                    color="#66736B",
                ),

                ft.Row(
                    controls=[
                        question,

                        ft.Button(
                            content="Ask AI",
                            on_click=ask_ai,
                        ),
                    ],
                    spacing=10,
                ),

                ft.Container(
                    content=answer,
                    padding=20,
                    bgcolor="#E8F5EE",
                    border_radius=10,
                ),
            ],
            spacing=15,
        ),
        margin=ft.Margin.symmetric(
            horizontal=60,
            vertical=25,
        ),
        padding=25,
        bgcolor="#FFFFFF",
        border_radius=12,
        border=ft.Border.all(
            1,
            "#DDE8E1",
        ),
    )

    # -----------------------------
    # FEATURE CARD FUNCTION
    # -----------------------------

    def make_card(icon, title, text):

        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(
                        icon,
                        size=35,
                    ),

                    ft.Text(
                        title,
                        size=19,
                        weight=ft.FontWeight.BOLD,
                        color="#064E3B",
                    ),

                    ft.Text(
                        text,
                        color="#66736B",
                    ),
                ],
                spacing=8,
            ),
            expand=True,
            padding=20,
            bgcolor="#FFFFFF",
            border_radius=10,
            border=ft.Border.all(
                1,
                "#DDE8E1",
            ),
        )

    # -----------------------------
    # FEATURE SECTION
    # -----------------------------

    features = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text(
                    "Simple ways to help 🌍",
                    size=25,
                    weight=ft.FontWeight.BOLD,
                    color="#064E3B",
                ),

                ft.Row(
                    controls=[
                        make_card(
                            "♻️",
                            "Waste",
                            "Reduce, reuse and recycle.",
                        ),

                        make_card(
                            "⚡",
                            "Energy",
                            "Use energy wisely.",
                        ),

                        make_card(
                            "💧",
                            "Water",
                            "Save water whenever possible.",
                        ),
                    ],
                    spacing=15,
                ),
            ],
            spacing=15,
        ),
        margin=ft.Margin.symmetric(
            horizontal=60,
            vertical=10,
        ),
    )

    # -----------------------------
    # FOOTER
    # -----------------------------

    footer = ft.Container(
        content=ft.Text(
            "GreenGuide • A greener tomorrow",
            color="#FFFFFF",
        ),
        padding=20,
        bgcolor="#064E3B",
        alignment=ft.Alignment.CENTER,
    )

    # -----------------------------
    # ADD EVERYTHING
    # -----------------------------

    page.add(
        ft.ListView(
            controls=[
                header,
                hero,
                ai_section,
                features,
                footer,
            ],
            expand=True,
            spacing=0,
        )
    )


# -----------------------------
# RUN
# -----------------------------

if __name__ == "__main__":
    ft.run(main)