from textual.app import App
from textual import events
from textual.view import View
from textual.widgets import Placeholder
from textual.layouts.grid import GridLayout


class GridTest(App):
    async def on_mount(self, event: events.Mount) -> None:
        """Create a grid with auto-arranging cells."""

        grid = await self.view.dock_grid()

        grid.add_column("col", fraction=1, max_size=20)
        grid.add_row("row", fraction=1, max_size=10)
        grid.set_repeat(True, True)
        grid.add_areas(center="col-2-start|col-4-end,row-2-start|row-3-end")
        grid.set_align("stretch", "center")

        grid.place(*(Placeholder() for _ in range(20)), center=Placeholder())


GridTest.run(title="Grid Test", log="textual.log")
