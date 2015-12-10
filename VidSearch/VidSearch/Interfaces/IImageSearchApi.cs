using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Controls;

namespace VidSearch.Interfaces
{
    interface IImageSearchApi
    {
        List<Image> search(string entityLabel);
    }
}
