using System;
using AutoMapper;
using Common;
using Common.Model.<#package#>;
using Microsoft.EntityFrameworkCore;
using Persistence;
using Persistence.<#package#>;
using Persistence.Repositories;

namespace Persistence<#package#>.Repositories
{
    public class <#name#>Repository : Repository<<#name#>Entity, <#name#>>,
        I<#name#>Repository
    {
        private readonly Lazy<WaWiContext> _context;
        protected override DbContext Context => _context.Value;

        public <#name#>Repository(Lazy<WaWiContext> context, IMapper mapper) : base(mapper, currentUser)
        {
            _context = context;
        }
    }
}