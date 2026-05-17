class Renderer:
    @staticmethod
    def draw_text(
        screen,
        text,
        font,
        color,
        x,
        y,
    ):
        rendered = font.render(
            text,
            True,
            color
        )

        screen.blit(rendered, (x, y))