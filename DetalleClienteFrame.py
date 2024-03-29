#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
# generated by wxGlade 0.6.5 (standalone edition) on Thu Mar 14 15:42:58 2013

import wx

# begin wxGlade: extracode
# end wxGlade



class MyDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyDialog.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyDialog.__set_properties
        self.SetTitle("dialog_1")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyDialog.__do_layout
        self.Layout()
        # end wxGlade

# end of class MyDialog

class FrameDescuento(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: FrameDescuento.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.panel_3 = wx.Panel(self, -1)
        self.label_10 = wx.StaticText(self.panel_3, -1, "Porcentaje")
        self.TextoPorcentaje = wx.TextCtrl(self.panel_3, -1, "")
        self.panel_4 = wx.Panel(self, -1)
        self.BtnCancelar = wx.Button(self.panel_4, -1, "Cancelar")
        self.Btn = wx.Button(self.panel_4, -1, "Aceptar")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: FrameDescuento.__set_properties
        self.SetTitle("frame_2")
        self.label_10.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.TextoPorcentaje.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.BtnCancelar.SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: FrameDescuento.__do_layout
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_7 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_9 = wx.FlexGridSizer(1, 2, 0, 0)
        grid_sizer_8 = wx.FlexGridSizer(1, 2, 0, 0)
        grid_sizer_8.Add(self.label_10, 0, wx.ALL, 8)
        grid_sizer_8.Add(self.TextoPorcentaje, 0, wx.RIGHT | wx.TOP | wx.BOTTOM, 8)
        self.panel_3.SetSizer(grid_sizer_8)
        sizer_7.Add(self.panel_3, 1, wx.EXPAND, 0)
        grid_sizer_9.Add(self.BtnCancelar, 0, wx.ALL, 5)
        grid_sizer_9.Add(self.Btn, 0, wx.ALL, 5)
        self.panel_4.SetSizer(grid_sizer_9)
        sizer_7.Add(self.panel_4, 1, wx.EXPAND, 0)
        sizer_2.Add(sizer_7, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_2)
        sizer_2.Fit(self)
        self.Layout()
        # end wxGlade

# end of class FrameDescuento
class FrameDetalleCliente(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: FrameDetalleCliente.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.panel_2 = wx.Panel(self, -1)
        self.label_1 = wx.StaticText(self.panel_2, -1, "CLIENTE")
        self.label_2 = wx.StaticText(self.panel_2, -1, "DNI")
        self.TextoDni = wx.TextCtrl(self.panel_2, -1, "")
        self.label_3 = wx.StaticText(self.panel_2, -1, "Nombre")
        self.TextoNombre = wx.TextCtrl(self.panel_2, -1, "")
        self.label_4 = wx.StaticText(self.panel_2, -1, u"Direcci�n")
        self.TextoDireccion = wx.TextCtrl(self.panel_2, -1, "")
        self.label_4_copy = wx.StaticText(self.panel_2, -1, "Telefono")
        self.TextoTelefono = wx.TextCtrl(self.panel_2, -1, "")
        self.label_4_copy_1 = wx.StaticText(self.panel_2, -1, "e-mail   ")
        self.TextoE-mail = wx.TextCtrl(self.panel_2, -1, "")
        self.panel_1 = wx.Panel(self, -1)
        self.static_line_1 = wx.StaticLine(self.panel_1, -1, style=wx.LI_VERTICAL)
        self.label_5 = wx.StaticText(self.panel_1, -1, "Resumen Cuenta")
        self.list_ctrl_1 = wx.ListCtrl(self.panel_1, -1, style=wx.LC_REPORT | wx.SUNKEN_BORDER)
        self.BtnEliminarAccion = wx.Button(self.panel_1, -1, u"Eliminar\nAcci�n")
        self.BtnEliminarCondicional = wx.Button(self.panel_1, -1, "Eliminar\nCondicional")
        self.label_6 = wx.StaticText(self.panel_1, -1, "Saldo")
        self.label_7 = wx.StaticText(self.panel_1, -1, "")
        self.label_8 = wx.StaticText(self.panel_1, -1, "Entrega")
        self.TextoEntrada = wx.TextCtrl(self.panel_1, -1, "")
        self.label_8_copy = wx.StaticText(self.panel_1, -1, "Paga con")
        self.TextoPagaCon = wx.TextCtrl(self.panel_1, -1, "")
        self.label_8_copy_copy = wx.StaticText(self.panel_1, -1, "Vuelto")
        self.label_9 = wx.StaticText(self.panel_1, -1, "")
        self.BtnCancelar = wx.Button(self.panel_1, -1, "Cancelar")
        self.BtnAceptar = wx.Button(self.panel_1, -1, "Aceptar")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: FrameDetalleCliente.__set_properties
        self.SetTitle("Detalle Cliente")
        self.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.label_1.SetFont(wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.label_2.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.TextoDni.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.label_3.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.TextoNombre.SetMinSize((200, 31))
        self.TextoNombre.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.label_4.SetMinSize((65, 25))
        self.label_4.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.TextoDireccion.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.label_4_copy.SetMinSize((65, 25))
        self.label_4_copy.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.TextoTelefono.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.label_4_copy_1.SetMinSize((65, 25))
        self.label_4_copy_1.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.TextoE-mail.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.panel_2.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 1, ""))
        self.label_5.SetFont(wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.list_ctrl_1.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.BtnEliminarAccion.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.BtnEliminarCondicional.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.label_6.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.label_7.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.label_8.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.TextoEntrada.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.label_8_copy.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.TextoPagaCon.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.label_8_copy_copy.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.label_9.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: FrameDetalleCliente.__do_layout
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_5 = wx.BoxSizer(wx.VERTICAL)
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_7 = wx.FlexGridSizer(1, 2, 0, 0)
        grid_sizer_6 = wx.FlexGridSizer(1, 6, 0, 0)
        grid_sizer_1 = wx.FlexGridSizer(1, 2, 0, 0)
        grid_sizer_4 = wx.FlexGridSizer(1, 2, 0, 0)
        sizer_6 = wx.BoxSizer(wx.VERTICAL)
        sizer_4 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_3_copy_1 = wx.FlexGridSizer(1, 2, 0, 0)
        grid_sizer_3_copy = wx.FlexGridSizer(1, 2, 0, 0)
        grid_sizer_3 = wx.FlexGridSizer(1, 2, 0, 0)
        grid_sizer_2 = wx.FlexGridSizer(1, 5, 0, 0)
        sizer_4.Add(self.label_1, 0, wx.LEFT, 7)
        grid_sizer_2.Add(self.label_2, 0, wx.LEFT | wx.TOP, 10)
        grid_sizer_2.Add(self.TextoDni, 0, wx.LEFT | wx.TOP, 8)
        grid_sizer_2.Add(self.label_3, 0, wx.LEFT | wx.TOP, 10)
        grid_sizer_2.Add(self.TextoNombre, 0, wx.LEFT | wx.TOP, 8)
        grid_sizer_2.AddGrowableCol(3)
        sizer_4.Add(grid_sizer_2, 1, wx.EXPAND, 0)
        grid_sizer_3.Add(self.label_4, 0, wx.LEFT | wx.TOP, 10)
        grid_sizer_3.Add(self.TextoDireccion, 0, wx.LEFT | wx.RIGHT | wx.TOP | wx.EXPAND, 8)
        grid_sizer_3.AddGrowableCol(1)
        sizer_4.Add(grid_sizer_3, 1, wx.EXPAND, 0)
        grid_sizer_3_copy.Add(self.label_4_copy, 0, wx.LEFT | wx.TOP, 10)
        grid_sizer_3_copy.Add(self.TextoTelefono, 0, wx.LEFT | wx.RIGHT | wx.TOP | wx.EXPAND, 8)
        grid_sizer_3_copy.AddGrowableCol(1)
        sizer_4.Add(grid_sizer_3_copy, 1, wx.EXPAND, 0)
        grid_sizer_3_copy_1.Add(self.label_4_copy_1, 0, wx.LEFT | wx.TOP, 10)
        grid_sizer_3_copy_1.Add(self.TextoE-mail, 0, wx.LEFT | wx.RIGHT | wx.TOP | wx.EXPAND, 9)
        grid_sizer_3_copy_1.AddGrowableCol(1)
        sizer_4.Add(grid_sizer_3_copy_1, 1, wx.EXPAND, 0)
        self.panel_2.SetSizer(sizer_4)
        sizer_3.Add(self.panel_2, 1, wx.EXPAND, 8)
        sizer_5.Add(self.static_line_1, 0, wx.EXPAND, 0)
        sizer_5.Add(self.label_5, 0, wx.LEFT | wx.RIGHT | wx.BOTTOM, 5)
        grid_sizer_4.Add(self.list_ctrl_1, 1, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_VERTICAL, 6)
        sizer_6.Add(self.BtnEliminarAccion, 0, wx.ALL, 5)
        sizer_6.Add(self.BtnEliminarCondicional, 0, wx.ALL, 5)
        grid_sizer_4.Add(sizer_6, 1, wx.EXPAND, 0)
        grid_sizer_4.AddGrowableCol(0)
        sizer_5.Add(grid_sizer_4, 1, wx.EXPAND, 0)
        grid_sizer_1.Add(self.label_6, 0, wx.LEFT | wx.RIGHT | wx.TOP, 5)
        grid_sizer_1.Add(self.label_7, 0, wx.TOP, 5)
        sizer_1.Add(grid_sizer_1, 1, wx.EXPAND, 0)
        grid_sizer_6.Add(self.label_8, 0, wx.ALL, 4)
        grid_sizer_6.Add(self.TextoEntrada, 0, wx.RIGHT | wx.TOP | wx.BOTTOM, 3)
        grid_sizer_6.Add(self.label_8_copy, 0, wx.ALL, 4)
        grid_sizer_6.Add(self.TextoPagaCon, 0, wx.RIGHT | wx.TOP | wx.BOTTOM, 3)
        grid_sizer_6.Add(self.label_8_copy_copy, 0, wx.ALL, 4)
        grid_sizer_6.Add(self.label_9, 0, wx.ALL, 4)
        sizer_1.Add(grid_sizer_6, 1, wx.EXPAND, 0)
        grid_sizer_7.Add(self.BtnCancelar, 0, wx.ALL | wx.ALIGN_RIGHT, 4)
        grid_sizer_7.Add(self.BtnAceptar, 0, wx.ALL, 4)
        grid_sizer_7.AddGrowableCol(0)
        sizer_1.Add(grid_sizer_7, 1, wx.EXPAND, 0)
        sizer_5.Add(sizer_1, 1, wx.EXPAND, 0)
        self.panel_1.SetSizer(sizer_5)
        sizer_3.Add(self.panel_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_3)
        sizer_3.Fit(self)
        self.Layout()
        # end wxGlade

# end of class FrameDetalleCliente
if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_1 = FrameDetalleCliente(None, -1, "")
    app.SetTopWindow(frame_1)
    frame_1.Show()
    app.MainLoop()
