from pymol import cmd


def coloraf_lr(selection="all"):

    """
    AUTHOR
    Christian Balbin

    DESCRIPTION
    Colors Alphafold structures by pLDDT

    USAGE
    coloraf sele

    PARAMETERS

    sele (string)
    The name of the selection/object to color by pLDDT. Default: all
    """

    cmd.color("blue", f"({selection}) and b > 90")
    cmd.color("cyan", f"({selection}) and b < 90 and b > 70")
    cmd.color("yellow", f"({selection}) and b < 70 and b > 50")
    cmd.color("orange", f"({selection}) and b < 50")

def coloraf_hr(selection="all"):

    """
    AUTHOR
    Christian Balbin

    DESCRIPTION
    Colors Alphafold structures by pLDDT

    USAGE
    coloraf sele

    PARAMETERS

    sele (string)
    The name of the selection/object to color by pLDDT. Default: all
    """

    cmd.color("blue", f"({selection}) and b > 95")
    cmd.color("cyan", f"({selection}) and b < 95 and b > 85")
    cmd.color("yellow", f"({selection}) and b < 85 and b > 70")
    cmd.color("orange", f"({selection}) and b < 70")

cmd.extend("coloraf_lr", coloraf_lr)
cmd.extend("coloraf_hr", coloraf_hr)

cmd.auto_arg[0]["coloraf_lr"] = [cmd.object_sc, "object", ""]
cmd.auto_arg[0]["coloraf_hr"] = [cmd.object_sc, "object", ""]
