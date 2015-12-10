using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Controls;
using VidSearch.Interfaces;

namespace VidSearch
{
    interface Logic
    {
        private IImageMatcher imageMatcher { get; set; }
        private IImageSearchApi imageSearchApi { get; set; }

        private ISplittableVideo video{get; set;}

        public List<IFrame> searchEntity(string videoPath, string entityLabel)
        {
            List<Image> entitySamples = imageSearchApi.search(entityLabel);
            return imageMatcher.findMatches(video.split(), entitySamples);
        }
    }
}
