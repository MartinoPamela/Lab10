import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._currentCountry = None

    def handleCalcola(self, e):
        year = self._view._txtAnno.value
        try:
            yearN = int(year)
        except:
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(ft.Text("Please provide a numerical value in field. "))
            self._view.update_page()
            return

        if yearN < 1816 or yearN > 2016:
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(ft.Text("Please provide a value between 1816 and 2016. "))
            self._view.update_page()
            return

        self._model.buildGraph(yearN)

        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(ft.Text("Grafo correttamente creato"))
        self._view._txt_result.controls.append(ft.Text(f"Il grafo ha {self._model.numCompConnesse()} componenti connesse"))
        self._view._txt_result.controls.append(ft.Text("Di seguito il dettaglio sui nodi:"))

        for n in self._model.getNodes():
            self._view._txt_result.controls.append(
                ft.Text(f"{n} -- {self._model.getNumConfinanti(n)} vicini."))

        self._fillDD()
        self._view._statoDD.disabled = False
        self._view._btnStatiRaggiungibili.disabled = False
        self._view.update_page()

    def _fillDD(self):
        allNodes = self._model.getNodes()
        for a in allNodes:
            self._view._statoDD.options.append(ft.dropdown.Option(text=a.StateNme,
                                                                  data=a,
                                                                  on_click=self._read_stato))

    def _read_stato(self, e):
        print("read_DD_Stato called ")
        if e.control.data is None:
            self._currentCountry = None
        else:
            self._currentCountry = e.control.data

        print(self._currentCountry)

    def handleRaggiungibili(self, e):

        visited = self._model.getBFSNodes(self._currentCountry)
        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(ft.Text(f"Da {self._currentCountry} è possibile "
                                                       f"raggiungere a piedi {len(visited)} stati: "))
        for v in visited:
            self._view._txt_result.controls.append(ft.Text(v))
        self._view.update_page()

